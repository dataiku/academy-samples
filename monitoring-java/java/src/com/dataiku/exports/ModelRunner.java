package com.dataiku.exports;

import java.io.*;
import java.nio.file.Files;
import java.util.*;

public class ModelRunner {

    private final ModelPredictor modelPredictor;

    private ModelRunner() {
        this.modelPredictor = new ModelPredictor();
    }

    public static void main(String[] args) {
        try {
            ModelRunner runFlow = new ModelRunner();
            runFlow.process();
        } catch (Exception e) {
            System.out.println("An error occurred: " + e.getMessage());
            e.printStackTrace();
        }
    }

    private String[] getRecordFromLine(String line) {
        List<String> values = new ArrayList<>();
        try (Scanner rowScanner = new Scanner(line)) {
            rowScanner.useDelimiter(";");
            while (rowScanner.hasNext()) {
                values.add(rowScanner.next());
            }
        }
        return values.toArray(new String[0]);
    }
    private List<String[]> readCSVContent(File fileToRead) throws FileNotFoundException {
        List<String[]> records = new ArrayList<>();
        try (Scanner scanner = new Scanner(fileToRead);) {
            // Skip header line
            if (scanner.hasNextLine()) {
                scanner.nextLine();
            }
            while (scanner.hasNextLine()) {
                records.add(getRecordFromLine(scanner.nextLine()));
            }
        }
        return records;
    }
    private String[] readCSVHeader(File fileToRead) throws FileNotFoundException {
        try (Scanner scanner = new Scanner(fileToRead);) {
            if (scanner.hasNextLine()) {
                return getRecordFromLine(scanner.nextLine());
            }
        }
        throw new RuntimeException("Input data file has no row to process");
    }
    private void process() throws IOException {
        String inputData = "java/input/pokemon_for_scoring.csv";
        String predDir = "java/output/java/";
        File inputDataFile = new File(inputData);
        File predDirFile = new File(predDir);
        Files.createDirectories(predDirFile.toPath());

        // Load data from input file
        System.out.println("Processing file " + inputDataFile.getAbsolutePath());
        List<String[]> inputDataset = readCSVContent(inputDataFile);
        String[] header = readCSVHeader(inputDataFile);
        System.out.println("Loaded input data with " + inputDataset.size() + " rows and header " + Arrays.toString(header));

        // Make predictions
        List<List<String>> outputDataset = modelPredictor.predictBatch(inputDataset, header);
        System.out.println("Predictions done, storing prediction logs");

        //Export prediction logs
        List<String> outputHeader = new ArrayList<>(Arrays.asList(header));
        outputHeader.add("prediction");

        FileWriter outputFileWriter = new FileWriter(predDir + "pokemon_scored_java.csv");
        outputFileWriter.write(String.join(", ", outputHeader) + System.lineSeparator());
        for (List<String> pred : outputDataset) {
            outputFileWriter.write(String.join(", ", pred) + System.lineSeparator());
        }
        outputFileWriter.close();
    }
}