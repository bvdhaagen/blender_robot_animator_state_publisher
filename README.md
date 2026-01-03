# blender_robot_animation_state_publisher
A Blender Python script for exporting robot joint angles to CSV/JSON formats, specifically designed for ROS (Robot Operating System) and robot control applications.


    Compatible with Blender 5.0+

🚀 Installation

    Copy the script to your Blender script directory or use inline execution

    For use in Blender Script Editor:

        Open Blender

        Go to Scripting workspace

        Open a new text editor

        Paste the script "blender_animate.py" and save the file

        Click Run Script

🎯 Usage
Requirements in Blender before you run the script

    Change : your_user_name around line 21 of the script  >>   export_dir = os.path.join(home, "your_user_name", "Desktop", "blender_ros_exports")

    Armature: A robot model with armature (skeleton)

    Animation: Keyframes for the desired movement

    Selection: Select the armature in the 3D viewport

    Mode: Ensure Blender is in Pose Mode


Files created:

    ik_bone_matrices.json - Complete bone matrices data

    joint_angles_degrees.json - Joint angles in JSON format

    joint_angles_full.csv - All angles (X,Y,Z) for each joint

    joint_angles_z_only.csv - Only Z-angles (for 2D robot arms)

    joint_angles_separated.csv - Separate columns per axis



   
    you can also generate animations based on keyframes you can copy from blender and output the CSV in the workspace  (> goliath_amination_gerator.py script) 

    Paste the CSV in the in the workspace (undere how you called the workspace  -- not under "src")
    
    publish the jointstates to check if evetything is working as expected before you launch the joint position commander 

    happy movements is a happy robot!!

    

    
