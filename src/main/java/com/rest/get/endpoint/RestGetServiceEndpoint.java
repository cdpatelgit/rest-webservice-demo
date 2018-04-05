package com.rest.get.endpoint;

import java.io.File;
import java.io.IOException;

import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.fasterxml.jackson.annotation.JsonAutoDetect.Visibility;
import com.fasterxml.jackson.annotation.PropertyAccessor;
import com.fasterxml.jackson.core.JsonParseException;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

@CrossOrigin
@RestController
public class RestGetServiceEndpoint {
	
	@RequestMapping(value="/circuitdetail",
					produces = MediaType.APPLICATION_JSON_VALUE,
					method = RequestMethod.GET)
	 public String requestCircuitDetails(@RequestParam(value="ckt")String circuitName) throws JsonProcessingException{
		CircuitDetail cktDetails = new CircuitDetail(circuitName, "ABCD");
		ObjectMapper mapper = new ObjectMapper();
		String json = mapper.writeValueAsString(cktDetails);
		return json;
		 
	 }
	
	
	@RequestMapping(value="CDX",
			produces = MediaType.APPLICATION_JSON_VALUE,
			method = RequestMethod.GET)
	public String requestCircuitDetails1(){
		System.out.println("RestGetServiceEndpoint: requestCircuitDetails1");
	//return "{\"name\":\"On Screen CDX\"}";
		return getJsonData("c:\\PrimeNGJson.json");
	 
	}
	
	@RequestMapping(value="/WA",
			produces = MediaType.APPLICATION_JSON_VALUE,
			method = RequestMethod.GET)
	public String requestCircuitDetails2() throws JsonParseException, IOException{
		System.out.println("RestGetServiceEndpoint: requestCircuitDetails2");
	return getJsonData("c:\\GetConnectionResponse.json");
	 
	}
	
	
	private String getJsonData(String fileName)  {
		ObjectMapper mapper = new ObjectMapper();
		String jsonData = "";
		try {
			
			
			
			mapper.setVisibility(PropertyAccessor.FIELD, Visibility.ANY);
			jsonData = mapper.writerWithDefaultPrettyPrinter().writeValueAsString(mapper.readTree(new File(fileName)));
			System.out.println("ScreenController: getJsonData: " + jsonData);
		} catch (JsonProcessingException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		return jsonData;
	}

}
