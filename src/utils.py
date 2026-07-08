import cv2
import time
from datetime import datetime

class FPS:
    """FPS calculator for real-time applications"""
    def __init__(self):
        self.start_time = None
        self.frame_count = 0
        self.fps = 0
        
    def update(self):
        """Update FPS calculation"""
        if self.start_time is None:
            self.start_time = time.time()
            return self.fps
            
        self.frame_count += 1
        elapsed_time = time.time() - self.start_time
        
        if elapsed_time > 0:
            self.fps = self.frame_count / elapsed_time
            
        return self.fps
    
    def reset(self):
        """Reset FPS counter"""
        self.start_time = time.time()
        self.frame_count = 0
        self.fps = 0

def get_current_time():
    """Get current timestamp for file naming"""
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def resize_frame(frame, width=640):
    """Resize frame maintaining aspect ratio"""
    height = int(frame.shape[0] * (width / frame.shape[1]))
    return cv2.resize(frame, (width, height))