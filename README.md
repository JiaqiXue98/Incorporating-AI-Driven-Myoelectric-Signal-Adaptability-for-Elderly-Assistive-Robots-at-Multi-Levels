# Incorporating-AI-Driven-Myoelectric-Signal-Adaptability-for-Elderly-Assistive-Robots-at-Multi-Levels

# File Description 

The **'KD.ipynb'** is the training code for knowledge distillation (KD).

The **'KD_test.ipynb'** is the testing code for knowledge distillation.

The trained complete KD model is saved in  **'./checkpoint/'**.

The **'model_teacher_S.h5'** is the teacher model used in KD training.

The **'student_.h5'** is the obtained student model after KD.

The hand-elbow coordination data at the functional level is placed in **'./data_hand_and_elbow/'**.

The cooking data at the behavioral level is placed in **'./data_wok/'**.

The **'utilities'** can process EMG signals to create sliding windows. 

# Environment
The scripts are carried out on Tensorflow-2.6.0, Keras-2.6.0, and Python-3.6.5. 

# Usage

**Run the script 'KD.ipynb' to update a teacher model to a student model using knowledge distillation,enhancing its adaptability for a wider range of tasks.**


**Run the script 'KD_test.ipynb' to extract the student model and test its prediction performance of hand & elbow on old and new tasks.**

The accuracies are calculated and printed. The acc_h_target and acc_e_target represent the testing accuracies of hand and elbow motions on new cooking tasks, respectively. The acc_h_source and acc_e_source represent the testing accuracies of hand and elbow motions on old coordination tasks, respectively.   


