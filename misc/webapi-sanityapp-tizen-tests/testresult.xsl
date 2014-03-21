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
			<head>
				<script type="text/javascript" src="jquery.js" />
			</head>
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
					<div id="summary">
						<table>
							<tr>
								<th colspan="2">Test Summary</th>
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
								<td>Test Block</td>
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
						</table>
					</div>


					<div id="suite_summary">
						<div id="title">
							<a name="contents"></a>
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
								<th>Blocked</th>
								<th>Not Run</th>
								<th>Total</th>
							</tr>
							<xsl:for-each select="test_definition/suite">
								<xsl:sort select="@name" />
								<tr>
									<td>
										<a>
											<xsl:attribute name="href">
                                                                                      #<xsl:value-of
												select="@name" />
                                                                                   </xsl:attribute>
											<xsl:value-of select="@name" />
										</a>
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

					<div id="fail_cases">
						<div id="title">
							<table>
								<tr>
									<td class="title">
										<h1 align="center">
											Test Failures (
											<xsl:value-of
												select="count(test_definition/suite/set//testcase[@result = 'FAIL'])" />
											)
										</h1>
									</td>
								</tr>
							</table>
						</div>
						<xsl:for-each select="test_definition/suite">
							<xsl:sort select="@name" />
							<div id="btc">
								<a href="#contents">Back to Contents</a>
							</div>
							<div id="suite_title">
								Test Suite:
								<xsl:value-of select="@name" />
								<a>
									<xsl:attribute name="name">
                                          <xsl:value-of
										select="@name" />
                                    </xsl:attribute>
								</a>
							</div>
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
										<xsl:choose>
											<xsl:when test="@result">
												<xsl:if test="@result = 'FAIL'">

													<tr>
														<td>
															<xsl:value-of select="@id" />
														</td>
														<td>
															<xsl:value-of select="@purpose" />
														</td>


														<td class="red_rate">
															<xsl:value-of select="@result" />
														</td>

														<td>
															<xsl:value-of select=".//result_info/stdout" />
															<xsl:if test=".//result_info/stdout = ''">
																N/A
															</xsl:if>
														</td>
													</tr>
												</xsl:if>
											</xsl:when>
										</xsl:choose>
									</xsl:for-each>
								</xsl:for-each>
							</table>
						</xsl:for-each>
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
							<div id="btc">
								<a href="#contents">Back to Contents</a>
							</div>
							<div id="suite_title">
								Test Suite:
								<xsl:value-of select="@name" />
								<a>
									<xsl:attribute name="name">
                                                                     <xsl:value-of
										select="@name" />
                                                                  </xsl:attribute>
								</a>
							</div>
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
													<xsl:if test="@result != 'BLOCK' and @result != 'FAIL' and @result != 'PASS' ">
														<td>
															Not Run
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
				<div id="goTopBtn">
					<img border="0" src="./back_top.png" />
				</div>
				<script type="text/javascript" src="application.js" />
				<script language="javascript" type="text/javascript">
					$(document).ready(function(){
					goTopEx();
					});
				</script>
			</body>
		</html>
	</xsl:template>
	<xsl:template name="br-replace">
		<xsl:param name="word" />
		<xsl:variable name="cr">
			<xsl:text>
</xsl:text>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test="contains($word,$cr)">
				<xsl:value-of select="substring-before($word,$cr)" />
				<br />
				<xsl:call-template name="br-replace">
					<xsl:with-param name="word" select="substring-after($word,$cr)" />
				</xsl:call-template>
			</xsl:when>
			<xsl:otherwise>
				<xsl:value-of select="$word" />
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>
</xsl:stylesheet>
