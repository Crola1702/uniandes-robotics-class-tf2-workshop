# How to run

## 1. Complete TODO tasks

* **`turtle_tf2_broadcaster.py`**:
  * Initialize Transform broadcaster
  * Declare a subscriber to turtleX/pose topic
  * Set up transform message transform
  * Set up transform message rotation
  * Send transform message
* **`turtle_tf2_listener.py`**:
  * Initialize Transform listener
  * Declare a publisher to turtleX/cmd_vel topic
  * Create a timer to call the callback function
  * Calculate the angle difference between the turtles
  * Calculate the distance between the turtles
  * Publish the velocity message

## 2. Compile and source the workspace with colcon

```
colcon build --packages-select turtle_tf2
source install/setup.bash
```

## 3. Run launch file and move turtle1

Open 2 terminals. On the first one run:

```
ros2 run turtle_tf2 turtle_tf2_app.launch.yaml
```

On the second one run:
```
ros2 run turtlesim turtle_teleop_key
```

