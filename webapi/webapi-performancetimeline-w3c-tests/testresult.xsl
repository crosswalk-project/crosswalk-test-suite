<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:output method="html" version="1.0" encoding="UTF-8"
		indent="yes" />
	<xsl:template match="/">
		<html>
			<STYLE type="text/css">
				@import "tests.css";
			</STYLE>

			<body>
				<div id="testcasepage">
					<div id="title">
						<table>
							<tr>
								<td>
									<h1>Test Report</h1>
								</td>
							</tr>
						</table>
					</div>
					<div id="device">
						<table>
							<tr>
								<th colspan="2">Device Information</th>
							</tr>
							<tr>
								<td>Device Name</td>
								<td>
									<xsl:value-of select="test_definition/environment/@device_name" />
								</td>
							</tr>
							<tr>
								<td>Device Model</td>
								<td>
									<xsl:value-of select="test_definition/environment/@device_model" />
								</td>
							</tr>
							<tr>
								<td>OS Version</td>
								<td>
									<xsl:value-of select="test_definition/environment/@os_version" />
								</td>
							</tr>
							<tr>
								<td>Device ID</td>
								<td>
									<xsl:value-of select="test_definition/environment/@device_id" />
								</td>
							</tr>
							<tr>
								<td>Firmware Version</td>
								<td>
									<xsl:value-of select="test_definition/environment/@firmware_version" />
								</td>
							</tr>
							<tr>
								<td>Screen Size</td>
								<td>
									<xsl:value-of select="test_definition/environment/@screen_size" />
								</td>
							</tr>
							<tr>
								<td>Resolution</td>
								<td>
									<xsl:value-of select="test_definition/environment/@resolution" />
								</td>
							</tr>
							<tr>
								<td>Host Info</td>
								<td>
									<xsl:value-of select="test_definition/environment/@host" />
								</td>
							</tr>
							<tr>
								<td>Others</td>
								<td>
									<xsl:value-of select="test_definition/environment/other" />
								</td>
							</tr>
						</table>
					</div>

					<div id="summary">
						<table>
							<tr>
								<th colspan="2">Test Summary</th>
							</tr>
							<tr>
								<td>Test Plan Name</td>
								<td>
									<xsl:value-of select="test_definition/summary/@test_plan_name" />
								</td>
							</tr>
							<tr>
								<td>Tests Total</td>
								<td>
									<xsl:value-of select="count(test_definition//suite/set/testcase)" />
								</td>
							</tr>
							<tr>
								<td>Test Passed</td>
								<td>
									<xsl:value-of
										select="count(test_definition//suite/set/testcase[@result = 'PASS'])" />
								</td>
							</tr>
							<tr>
								<td>Test Failed</td>
								<td>
									<xsl:value-of
										select="count(test_definition//suite/set/testcase[@result = 'FAIL'])" />
								</td>
							</tr>
							<tr>
								<td>Test N/A</td>
								<td>
									<xsl:value-of
										select="count(test_definition//suite/set/testcase[@result = 'BLOCK'])" />
								</td>
							</tr>
							<tr>
								<td>Test Not Run</td>
								<td>
									<xsl:value-of
										select="count(test_definition//suite/set/testcase) - count(test_definition//suite/set/testcase[@result = 'PASS']) - count(test_definition//suite/set/testcase[@result = 'FAIL']) - count(test_definition//suite/set/testcase[@result = 'BLOCK'])" />
								</td>
							</tr>
							<tr>
								<td>Start time</td>
								<td>
									<xsl:value-of select="test_definition/summary/start_at" />
								</td>
							</tr>
							<tr>
								<td>End time</td>
								<td>
									<xsl:value-of select="test_definition/summary/end_at" />
								</td>
							</tr>
						</table>
					</div>


					<div id="suite_summary">
						<div id="title">
							<table>
								<tr>
									<td class="title">
										<h1>Test Summary by Suite</h1>
									</td>
								</tr>
							</table>
						</div>
						<table>
							<tr>
								<th>Suite</th>
								<th>Passed</th>
								<th>Failed</th>
								<th>N/A</th>
								<th>Not Run</th>
								<th>Total</th>
							</tr>
							<xsl:for-each select="test_definition/suite">
								<xsl:sort select="@name" />
								<tr>
									<td>
										<xsl:value-of select="@name" />
									</td>
									<td>
										<xsl:value-of select="count(set//testcase[@result = 'PASS'])" />
									</td>
									<td>
										<xsl:value-of select="count(set//testcase[@result = 'FAIL'])" />
									</td>
									<td>
										<xsl:value-of select="count(set//testcase[@result = 'BLOCK'])" />
									</td>
									<td>
										<xsl:value-of
											select="count(set//testcase) - count(set//testcase[@result = 'PASS']) - count(set//testcase[@result = 'FAIL']) - count(set//testcase[@result = 'BLOCK'])" />
									</td>
									<td>
										<xsl:value-of select="count(set//testcase)" />
									</td>
								</tr>
							</xsl:for-each>
						</table>
					</div>

					<div id="cases">
						<div id="title">
							<table>
								<tr>
									<td class="title">
										<h1 align="center">Detailed Test Results</h1>
									</td>
								</tr>
							</table>
						</div>
						<xsl:for-each select="test_definition/suite">
							<xsl:sort select="@name" />
							<p>
								Test Suite:
								<xsl:value-of select="@name" />
							</p>
							<table>
								<tr>
									<th>Case_ID</th>
									<th>Purpose</th>
									<th>Result</th>
									<th>Stdout</th>
								</tr>
								<xsl:for-each select=".//set">
									<xsl:sort select="@name" />
									<tr>
										<td colspan="4">
											Test Set:
											<xsl:value-of select="@name" />
										</td>
									</tr>
									<xsl:for-each select=".//testcase">
										<xsl:sort select="@id" />
										<tr>
											<td>
												<xsl:value-of select="@id" />
											</td>
											<td>
												<xsl:value-of select="@purpose" />
											</td>

											<xsl:choose>
												<xsl:when test="@result">
													<xsl:if test="@result = 'FAIL'">
														<td class="red_rate">
															<xsl:value-of select="@result" />
														</td>
													</xsl:if>
													<xsl:if test="@result = 'PASS'">
														<td class="green_rate">
															<xsl:value-of select="@result" />
														</td>
													</xsl:if>
													<xsl:if test="@result = 'BLOCK' ">
														<td>
															BLOCK
														</td>
													</xsl:if>
												</xsl:when>
												<xsl:otherwise>
													<td>

													</td>
												</xsl:otherwise>
											</xsl:choose>
											<td>
												<xsl:value-of select=".//result_info/stdout" />
												<xsl:if test=".//result_info/stdout = ''">
													N/A
												</xsl:if>
											</td>
										</tr>
									</xsl:for-each>
								</xsl:for-each>
							</table>
						</xsl:for-each>
					</div>
				</div>
			</body>
		</html>
	</xsl:template>
</xsl:stylesheet>