package com.rest.post.endpoint;

import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/value")
public class DMaapPostServiceEndpoint {
	
	@RequestMapping(value = "/update",
					consumes = MediaType.APPLICATION_JSON_VALUE,
					produces = MediaType.APPLICATION_JSON_VALUE,
					method = RequestMethod.POST)
	public String updateLocations(String jsonString){
		return "Location updated";
		
	}
	
	
	
	@RequestMapping(value = "/hello",
			consumes = MediaType.APPLICATION_JSON_VALUE,
			produces = MediaType.APPLICATION_JSON_VALUE,
			method = RequestMethod.POST)
	public String sayHello() {
		return "Hello DMaap";

	}

}
