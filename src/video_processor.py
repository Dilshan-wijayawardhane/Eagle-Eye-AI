import cv2
import sys
from pathlib import Path
from src.utils import FPS, resize_frame

class VideoProcessor:
    """Handles video input from webcam or file"""
    
    def __init__(self, source=0, width=640, height=480):
        """
        Initialize video processor
        
        Args:
            source: Video source (0 for webcam, or file path)
            width: Frame width
            height: Frame height
        """
        self.source = source
        self.width = width
        self.height = height
        self.cap = None
        self.fps_calculator = FPS()
        self.is_webcam = isinstance(source, int) or source == '0'
        
    def open(self):
        """Open video capture"""
        try:
            if self.is_webcam:
                # Webcam
                source_int = int(self.source) if isinstance(self.source, str) else self.source
                self.cap = cv2.VideoCapture(source_int)
            else:
                # Video file
                video_path = Path(self.source)
                if not video_path.exists():
                    raise FileNotFoundError(f"Video file not found: {self.source}")
                self.cap = cv2.VideoCapture(str(video_path))
                
            if not self.cap.isOpened():
                raise Exception("Could not open video source")
                
            # Set resolution for webcam
            if self.is_webcam:
                self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
                self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
                
            print(f"✅ Video source opened: {self.source}")
            return True
            
        except Exception as e:
            print(f"❌ Error opening video source: {e}")
            return False
            
    def get_frame(self):
        """
        Get next frame from video source
        
        Returns:
            frame: Next frame or None if end of video
        """
        if self.cap is None:
            return None
            
        ret, frame = self.cap.read()
        if not ret:
            return None
            
        # Resize frame for consistent processing
        frame = resize_frame(frame, self.width)
        
        # Update FPS
        fps = self.fps_calculator.update()
        
        return frame, fps
        
    def get_video_properties(self):
        """Get video properties"""
        if self.cap is None:
            return None
            
        properties = {
            'width': int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            'height': int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
            'fps': self.cap.get(cv2.CAP_PROP_FPS),
            'frame_count': int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        }
        return properties
        
    def release(self):
        """Release video capture resources"""
        if self.cap is not None:
            self.cap.release()
            print("✅ Video resources released")
            
    def __del__(self):
        """Cleanup on object destruction"""
        self.release()