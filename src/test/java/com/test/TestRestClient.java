package com.test;

import org.junit.Ignore;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.TestConfiguration;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.http.ResponseEntity;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.web.util.UriComponentsBuilder;

import com.boot.application.Application;
import com.rest.post.client.NotifyDMaapService;
import com.rest.post.client.NotifyDMaapServiceImpl;

import io.swagger.util.Json;

import java.util.Collections;

@ContextConfiguration(classes = {Application.class, TestConfiguration.class,NotifyDMaapServiceImpl.class})
@ComponentScan(basePackages = {"com.rest"})
@RunWith(SpringRunner.class)
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.DEFINED_PORT, properties = {"server.port=7070"})

public class TestRestClient {
	
	
	@Autowired
	NotifyDMaapService notifyDMaapService;
	
	@Autowired
	TestRestTemplate restTemplate;
	
	@Ignore
	@Test
	public void testRestClient() 
	{
		notifyDMaapService.notifyToDMaapServiceForUpdatedLocation();
		
		Json.prettyPrint("");
	}
	
	
	@Ignore
	@Test
	public void testPostRestClient1() 
	{
		
		UriComponentsBuilder builder = UriComponentsBuilder.fromHttpUrl("http://localhost:7070/value/hello");
		restTemplate.postForEntity(builder.build().encode().toUri(), "Hi", String.class);

		Json.prettyPrint("");
	}
	
	@Test
	public void testGetRestClient() 
	{
		
		UriComponentsBuilder builder = UriComponentsBuilder.fromHttpUrl("http://localhost:7070/circuitdetail?ckt=UNIA");
		ResponseEntity<String> response = restTemplate.getForEntity(builder.build().encode().toUri(), String.class);
		
		Json.prettyPrint(response);
	}
	
	

}
