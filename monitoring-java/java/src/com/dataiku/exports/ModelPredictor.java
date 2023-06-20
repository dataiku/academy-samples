package com.dataiku.exports;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.dataiku.scoring.*;
import com.dataiku.sample.GreatModel;


public class ModelPredictor {

    public List<List<String>> predictBatch(List<String[]> rowsToPredict, String[] featureNames) {
        List<List<String>> outputDataset = new ArrayList<>();
         for(String[] rowsToPredic : rowsToPredict) {
            List<String> oRow = predict(rowsToPredic, featureNames);
            outputDataset.add(oRow);
        }
        return outputDataset;
    }

    private List<String> predict(String[] featureValues, String[] featureNames) {
        List<String> outputRow = new ArrayList<>(Arrays.asList(featureValues));
        GreatModel model = new GreatModel();
        Observation.Builder obsBuilder = model.observationBuilder();
        Map<String,String> features = new HashMap<>();
        for(int i = 0; i < featureNames.length; i++) {
            features.put(featureNames[i],featureValues[i]);
        }
        Observation obs = obsBuilder.withAll(features).build();
        if (obs.hasError()) {
            System.err.println("Can't build observation: " + obs.getErrorMessage());
            // maybe throw here
        }

        // For a classification model
        Try<ClassificationResult> prediction = model.predict(obs);
        if (prediction.isError()) {
            System.err.println("Can't make a prediction: " + prediction.getMessage());
            // maybe throw here
        } else {
            ClassificationResult result = prediction.get();
            // predictedClass is one of model.getClassLabels()
            String predictedClass = result.getPrediction();
            // probabilities has the same indices as model.getClassLabels()
            // i.e. 0 to (model.getNumClasses() - 1)
            double[] probabilities = result.getProbabilities();
            // Use result here
            System.out.println("Result of prediction is *" + predictedClass + "* ("  + Arrays.toString(probabilities) + ")");
            outputRow.add(predictedClass);
        }
        return outputRow;
    }    

}
