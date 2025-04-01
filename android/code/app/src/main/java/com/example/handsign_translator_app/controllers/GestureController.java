package com.example.handsign_translator_app.controllers;

import android.os.Handler;
import com.example.handsign_translator_app.bluetooth.BluetoothModule;
import com.example.handsign_translator_app.ml_module.GestureClassifier;
import com.example.handsign_translator_app.ml_module.GestureStabilityChecker;
import com.example.handsign_translator_app.models.Gesture;
import com.example.handsign_translator_app.utils.Constants;
import java.util.ArrayDeque;
import java.util.Deque;

public class GestureController {
    // Number of sensor readings to maintain in the sliding window
    private static final int STABILITY_WINDOW = Constants.STABILITY_WINDOW;
    // Delay between consecutive sensor readings (in milliseconds)
    private static final int SENSOR_READ_DELAY_MS = Constants.SENSOR_READ_DELAY_MS;

    // Deque to hold the history of sensor readings
    private Deque<double[]> flexReadingsHistory = new ArrayDeque<>();
    // Module responsible for obtaining sensor data from the glove
    private BluetoothModule bluetoothModule;
    // Module that performs gesture classification using TensorFlow Lite
    private GestureClassifier gestureClassifier;
    // Handler for scheduling periodic sensor readings
    private Handler handler = new Handler();
    // Listener to provide gesture detection updates to the UI
    private GestureListener listener;
    // Stores the currently detected gesture (if any)
    public Gesture currentGesture;

    /**
     * Interface definition for callbacks to be invoked when a gesture is detected
     * or when translation is in progress.
     *
     * Additionally, you might consider adding a callback like onSensorDataReceived(int[] data)
     * if you want to update the UI or log raw sensor data.
     */
    public interface GestureListener {
        void onGestureDetected(Gesture gesture);
        void onTranslationInProgress();
        void onNoDeviceConnected();
        void rawDataOutput(String data);
        // Optionally:
        // void onSensorDataReceived(int[] sensorData);
    }

    /**
     * Constructor for GestureController.
     */
    public GestureController(BluetoothModule bluetoothModule, GestureClassifier gestureClassifier, GestureListener listener) {
        this.bluetoothModule = bluetoothModule;
        this.gestureClassifier = gestureClassifier;
        this.listener = listener;
    }

    /**
     * Starts the periodic reading of sensor data.
     */
    public void start() {
        handler.post(runnable);
    }

    /**
     * Stops the periodic reading of sensor data.
     */
    public void stop() {
        handler.removeCallbacks(runnable);
    }

    /**
     * Runnable that reads sensor data, checks for gesture stability, and triggers classification.
     */
    private Runnable runnable = new Runnable() {
        @Override
        public void run() {
            boolean deviceConnected = bluetoothModule.isDeviceConnected();
            if (deviceConnected) {
                // Retrieve the latest sensor data from the Bluetooth module
                double[] currentFlexReadings = bluetoothModule.getGloveData();
                boolean isStable = false;
                if (currentFlexReadings.length != 0) {
                    // Add the new readings to the sliding window
                    flexReadingsHistory.addLast(currentFlexReadings);
                    // Maintain a fixed-size sliding window
                    if (flexReadingsHistory.size() > STABILITY_WINDOW) {
                        flexReadingsHistory.removeFirst();
                    }
                    // Check if the current gesture (based on recent sensor readings) is stable
                    isStable = flexReadingsHistory.size() >= STABILITY_WINDOW;
                }

                if (isStable) {
                    // Convert sensor readings from double[] to float[]
                    float[][] readingsArray = new float[flexReadingsHistory.size()][];
                    int index = 0;
                    for (double[] reading : flexReadingsHistory) {
                        float[] floatReading = new float[reading.length];
                        for (int i = 0; i < reading.length; i++) {
                            floatReading[i] = (float) reading[i];  // Convert each double to float
                        }
                        readingsArray[index++] = floatReading;
                    }

                    // Classify the gesture using the gesture classifier
                    Gesture gesture = gestureClassifier.classifyGesture(readingsArray);
                    currentGesture = gesture;

                    // Notify listener that a gesture has been detected
                    listener.onGestureDetected(gesture);
                } else {
                    currentGesture = null;
                    // Notify listener that translation is in progress (gesture unstable)
                    listener.onTranslationInProgress();
                }
            } else {
                listener.onNoDeviceConnected();
            }

            // Schedule the next sensor reading after the specified delay
            handler.postDelayed(this, SENSOR_READ_DELAY_MS);
        }
    };


    /**
     * Helper method to convert an array of integers to an array of floats.
     */
//    private double[] convertIntArrayToFloatArray(int[] intArray) {
//        float[] floatArray = new float[intArray.length];
//        for (int i = 0; i < intArray.length; i++) {
//            floatArray[i] = intArray[i];
//        }
//        return floatArray;
//    }
}