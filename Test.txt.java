import java.io.*;
import java.net.*;
import java.nio.file.*;
import java.util.*;

public class FileUploader {
    public static void main(String[] args) {
        try {
            // Specify the URL of the REST endpoint
            String endpointUrl = "http://example.com/api/upload";
            
            // Create a HttpClient
            HttpClient httpClient = HttpClient.newBuilder().build();

            // Create a multipart request
            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(endpointUrl))
                    .header("Content-Type", "multipart/form-data")
                    .POST(buildMultipartBody())
                    .build();

            // Send the request and get the response
            HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());

            // Print the response
            System.out.println("Response code: " + response.statusCode());
            System.out.println("Response body: " + response.body());
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }

    private static BodyPublisher buildMultipartBody() throws IOException {
        // Prepare the file to upload
        Path filePath = Paths.get("path/to/your/file.txt");
        byte[] fileContent = Files.readAllBytes(filePath);

        // Build the multipart body
        ByteArrayOutputStream bos = new ByteArrayOutputStream();
        PrintWriter writer = new PrintWriter(new OutputStreamWriter(bos, StandardCharsets.UTF_8));

        // Add file part
        writer.append("--Boundary\r\n");
        writer.append("Content-Disposition: form-data; name=\"file\"; filename=\"" + filePath.getFileName() + "\"\r\n");
        writer.append("Content-Type: application/octet-stream\r\n");
        writer.append("\r\n");
        writer.flush();
        bos.write(fileContent);
        bos.flush();
        writer.append("\r\n");
        writer.flush();

        // Add any additional form fields here if needed

        // End boundary
        writer.append("--Boundary--\r\n");
        writer.flush();

        return HttpRequest.BodyPublishers.ofByteArray(bos.toByteArray());
    }
}
