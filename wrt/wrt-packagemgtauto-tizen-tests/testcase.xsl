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
									<h1>Test Cases</h1>
								</td>
							</tr>
						</table>
					</div>
					<div id="suites">
						<table>
							<tr>
								<th>Test Suite</th>
								<th>Total</th>
								<th>Auto</th>
								<th>Manual</th>
							</tr>
							<tr>
								<td>
									Total
								</td>
								<td>
									<xsl:value-of select="count(test_definition/suite/set//testcase)" />
								</td>
								<td>
									<xsl:value-of
										select="count(test_definition/suite/set//testcase[@execution_type = 'auto'])" />
								</td>
								<td>
									<xsl:value-of
										select="count(test_definition/suite/set//testcase[@execution_type != 'auto'])" />
								</td>
							</tr>
							<xsl:for-each select="test_definition/suite">
								<tr>
									<td>
										<xsl:value-of select="@name" />
									</td>
									<td>
										<xsl:value-of select="count(set//testcase)" />
									</td>
									<td>
										<xsl:value-of select="count(set/testcase[@execution_type = 'auto'])" />
									</td>
									<td>
										<xsl:value-of select="count(set/testcase[@execution_type != 'auto'])" />
									</td>
								</tr>
							</xsl:for-each>
						</table>
					</div>
					<div id="title">
						<table>
							<tr>
								<td class="title">
									<h1>Detailed Test Cases</h1>
								</td>
							</tr>
						</table>
					</div>
					<div id="cases">
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
									<th>Type</th>
									<th>Component</th>
									<th>Execution Type</th>
									<th>Description</th>
									<th>Specification</th>
								</tr>
								<xsl:for-each select=".//set">
									<xsl:sort select="@name" />
									<tr>
										<td colspan="7">
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
											<td>
												<xsl:value-of select="@type" />
											</td>
											<td>
												<xsl:value-of select="@component" />
											</td>
											<td>
												<xsl:value-of select="@execution_type" />
											</td>
											<td>
												<p>
													Pre_condition:
													<xsl:value-of select=".//description/pre_condition" />
												</p>
												<p>
													Post_condition:
													<xsl:value-of select=".//description/post_condition" />
												</p>
												<p>
													Test Script Entry:
													<xsl:value-of select=".//description/test_script_entry" />
												</p>
												<p>
													Steps:
													<p />
													<xsl:for-each select=".//description/steps/step">
														<xsl:sort select="@order" />
														Step
														<xsl:value-of select="@order" />
														:
														<xsl:value-of select="./step_desc" />
														;
														<p />
														Expected Result:
														<xsl:value-of select="./expected" />
														<p />
													</xsl:for-each>
												</p>
											</td>
											<td>
												<xsl:call-template name="br-replace">
													<xsl:with-param name="word" select=".//spec" />
												</xsl:call-template>
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