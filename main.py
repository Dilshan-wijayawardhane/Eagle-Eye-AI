import cv2
import argparse
import sys
import warnings
import os
from pathlib import Path

# Suppress warnings for cleaner output
warnings.filterwarnings("ignore")
os.environ['PYTORCH_ENABLE_MPS_FALLBACK'] = '1'
os.environ['ULTRALYTICS_VERBOSE'] = 'False'

# Add src to path
sys.path.append(str(Path(__file__).parent))

from src.detector import ObjectDetector
from src.video_processor import VideoProcessor
from src.utils import FPS



def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='Real-time Object Detection with YOLO')
    
    parser.add_argument('--source', type=str, default='0',
                       help='Video source: 0 for webcam, or path to video file')
    
    parser.add_argument('--model', type=str, default='yolov8n.pt',
                       help='Path to YOLO model weights')
    
    parser.add_argument('--confidence', type=float, default=0.5,
                       help='Confidence threshold for detections (0-1)')
    
    parser.add_argument('--width', type=int, default=640,
                       help='Frame width')
    
    parser.add_argument('--height', type=int, default=480,
                       help='Frame height')
    
    parser.add_argument('--save', action='store_true',
                       help='Save output video')
    
    return parser.parse_args()

def draw_info(frame, fps, detections_count):
    """Draw information overlay on frame"""
    # FPS
    cv2.putText(frame, f'FPS: {fps:.1f}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    # Detection count
    cv2.putText(frame, f'Detections: {detections_count}', (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    # Instructions
    cv2.putText(frame, 'Press Q to quit', (frame.shape[1] - 150, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

def main():
    """Main application entry point"""
    # Parse arguments
    args = parse_arguments()
    
    print("=" * 50)
    print("🎯 Real-Time Object Detection Application")
    print("=" * 50)
    print(f"📹 Source: {args.source}")
    print(f"🤖 Model: {args.model}")
    print(f"🎯 Confidence: {args.confidence}")
    print("=" * 50)
    
    # Initialize detector
    try:
        detector = ObjectDetector(
            model_path=args.model,
            confidence=args.confidence
        )
    except Exception as e:
        print(f"❌ Failed to initialize detector: {e}")
        return
    
    # Initialize video processor
    video_proc = VideoProcessor(
        source=args.source,
        width=args.width,
        height=args.height
    )
    
    if not video_proc.open():
        return
    
    # Video writer for saving
    writer = None
    if args.save:
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        writer = cv2.VideoWriter('output.avi', fourcc, 20.0, (args.width, args.height))
        print("💾 Output will be saved to 'output.avi'")
    
    print("\n🚀 Starting detection... Press 'q' or 'ESC' to quit\n")
    
    # Main loop
    try:
        while True:
            # Get frame
            frame, fps = video_proc.get_frame()
            
            if frame is None:
                print("End of video stream")
                break
            
            # Run detection
            results, annotated_frame, detections = detector.detect(frame)
            
            # Draw info overlay
            draw_info(annotated_frame, fps, len(detections))
            
            # Display detections in console (every 30 frames)
            if int(fps) % 30 == 0 and len(detections) > 0:
                print(f"\rDetected: {len(detections)} objects", end='')
            
            # Show frame
            cv2.imshow('Object Detection', annotated_frame)
            
            # Save frame if enabled
            if writer is not None:
                writer.write(annotated_frame)
            
            # Break loop on key press
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q') or key == 27:  # q or ESC
                print("\n🛑 Stopped by user")
                break
                
    except KeyboardInterrupt:
        print("\n🛑 Stopped by user (Ctrl+C)")
        
    except Exception as e:
        print(f"\n❌ Error during execution: {e}")
        
    finally:
        # Cleanup
        video_proc.release()
        if writer is not None:
            writer.release()
        cv2.destroyAllWindows()
        print("\n👋 Application closed")

if __name__ == "__main__":
    main()