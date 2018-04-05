package com.rest.post.client;

import org.springframework.stereotype.Component;
import org.springframework.web.client.RestTemplate;

@Component
public class NotifyDMaapServiceImpl implements NotifyDMaapService {

	//@Resource(name = "restTemplate")
	RestTemplate restTemplate;
	//@Value("${dmaap.endpoint.url}")
	private String dmaapHost;
	//@Value("${dmaap.endpoint.port}")
	private String dmaapPort;

	public static final String NOTIFY_DMAAP_SERVICE_RESOURCE = "/arm-endpoints/arm-search-resource/getAvailableUniServices";

	@Override
	public void notifyToDMaapServiceForUpdatedLocation() {

		// LOGGER.info("calling Notify DMaap Service for Updated Location..");

		String dammpEndpoint = "http://" + this.dmaapHost + ":" + this.dmaapPort + NOTIFY_DMAAP_SERVICE_RESOURCE;
		// LOGGER.debug("Calling DMaap endpoint by following address:" + dammpEndpoint);

		String jsonString = null;

		this.restTemplate.postForEntity(dammpEndpoint, jsonString, Object.class);

		// LOGGER.info("Notified DMaap Service for Updated Location.." + jsonString );

	}

}
