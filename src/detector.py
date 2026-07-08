from ultralytics import YOLO
import cv2
import numpy as np

class ObjectDetector:
    """YOLO-based object detector"""
    
    def __init__(self, model_path='yolov8n.pt', confidence=0.5):
        """
        Initialize the detector
        
        Args:
            model_path: Path to YOLO model weights
            confidence: Minimum confidence threshold for detections
        """
        self.confidence = confidence
        self.model = self.load_model(model_path)
        self.class_names = self.model.names
        
    def load_model(self, model_path):
        """
        Load YOLO model
        
        Args:
            model_path: Path to model weights
            
        Returns:
            Loaded YOLO model
        """
        try:
            model = YOLO(model_path)
            print(f"✅ Model loaded successfully: {model_path}")
            return model
        except Exception as e:
            print(f"❌ Error loading model: {e}")
            raise
            
    def detect(self, frame):
        """
        Run detection on a single frame
        
        Args:
            frame: Input image frame
            
        Returns:
            results: YOLO detection results
            annotated_frame: Frame with detections drawn
            detections: List of detection dictionaries
        """
        # Run inference
        results = self.model(frame, conf=self.confidence)
        
        # Get annotated frame
        annotated_frame = results[0].plot()
        
        # Extract detection details
        detections = []
        if results[0].boxes is not None:
            boxes = results[0].boxes
            for box in boxes:
                # Get box coordinates (xywh format)
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                confidence = float(box.conf[0])
                class_id = int(box.cls[0])
                class_name = self.class_names[class_id]
                
                detections.append({
                    'bbox': [int(x1), int(y1), int(x2), int(y2)],
                    'confidence': confidence,
                    'class_id': class_id,
                    'class_name': class_name
                })
        
        return results, annotated_frame, detections
        
    def detect_batch(self, frames):
        """
        Run detection on multiple frames
        
        Args:
            frames: List of frames
            
        Returns:
            List of detection results for each frame
        """
        results = []
        for frame in frames:
            _, annotated_frame, detections = self.detect(frame)
            results.append({
                'annotated_frame': annotated_frame,
                'detections': detections
            })
        return results