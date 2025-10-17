# stage-ui-td  
**A multimodal user interface for live creative programming in TouchDesigner**

---

## Overview  

**stage-ui-td** is a research prototype exploring **new ways to interact with creative coding environments** — specifically **TouchDesigner (TD)** — through **speech**, **gesture**, and **AI-assisted interface generation**.  

The system enables performers to manipulate visual programming networks on stage using natural gestures and spoken commands. By integrating **pose detection**, **speech-to-text parsing**, and **automatic widget generation**, stage-ui-td investigates how intelligent user interfaces can make complex creative software more responsive, expressive, and accessible during live performance.

---

## Project Goals  

- Develop an **on-stage interactive interface** for TouchDesigner that allows real-time parameter editing and network manipulation through natural input.  
- Explore **gesture-based and voice-driven programming** workflows.  
- Prototype **dynamic React-based widgets** generated directly from TouchDesigner components.  
- Evaluate usability and creative potential through **expert and performer-focused studies**.  

> **Note:** Next steps include researching graph completion for more complex TD networks.

---

## Research Contributions  

1. **Novel interaction paradigm:**  
   A new way to interface with existing creative programming tools (TouchDesigner) using multimodal input (pose, speech, and text).  

2. **On-stage interface for creative programming:**  
   A performer-oriented system that translates movement and spoken intent into UI actions.  

3. **LLM-based interpretation pipeline:**  
   Speech is processed via Whisper → parsed into JSON using a large language model → JSON objects either:  
   - Trigger **replicators** or widget creation, or  
   - Modify **existing widget parameters**.  

4. **Dynamic widget management system:**  
   - Uses heuristics (rank, layer depth) to show/hide controls dynamically.  
   - Stores widget history for quick reactivation.  

5. **Pose-driven control schema:**  
   - Starts with hand-based gestures, extendable to full-body poses.  
   - Evaluates intuitiveness and responsiveness of gesture–widget mapping.  

---

## System Architecture  

### 1. **User Interface (TouchDesigner)**
- Base component with *insertion points* (connections between compatible operator types).  
- Tracks:  
  - **Operator** type  
  - **Position**  
- Python callback generates a list of insertion points.  
- Enables **React widget generation** connected to TD parameters.  

### 2. **Speech Input (Whisper + Node.js)**
- TouchDesigner web client DAT sends microphone input to a Node.js server.  
- Whisper transcribes audio → sends text to backend for parsing.  
- Manual or whisper-triggered switches toggle pose detection.  

### 3. **Pose Detection (TFJS + MediaPipe Integration)**
- Chromium browser adapted from the MediaPipe plugin.  
- Uses TensorFlow.js and webcam feed for real-time skeleton tracking.  
- Outputs JSON pose data to TouchDesigner via WebSocket.  

### 4. **Widget Generation**
- React frontend built with:
  - `react-webcam`  
  - `html-react-parser`  
  - Custom detection canvas  
- Receives JSON describing TD parameters and builds interactive widgets dynamically.  
- Widgets can control TouchDesigner parameters or replicate nodes.  

---
