package com.rest.get.endpoint;

public class CircuitDetail {

	private final String cktName;

	private final String clo;

	public CircuitDetail(String cktName, String clo) {
		this.cktName = cktName;
		this.clo = clo;
	}

	public String getCktName() {
		return cktName;
	}

	public String getClo() {
		return clo;
	}

}
