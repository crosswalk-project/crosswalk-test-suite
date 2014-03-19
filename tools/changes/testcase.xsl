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
				<a name="top"/>
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
								<th>Add</th>
								<th>Update</th>
								<th>Remove</th>
							</tr>
							<tr>
								<td>
									Total
								</td>
								<td>
									<xsl:value-of select="count(test_definition/suite//testcase)" />
								</td>
								<td>
									<xsl:value-of
										select="count(test_definition/suite//testcase[@changes = 'Add'])" />
								</td>
								<td>
									<xsl:value-of
										select="count(test_definition/suite//testcase[@changes = 'Update'])" />
								</td>
								<td>
									<xsl:value-of
										select="count(test_definition/suite//testcase[@changes = 'Remove'])" />
								</td>
							</tr>
							<xsl:for-each select="test_definition/suite">
								<xsl:sort select="@name" />
								<tr>
									<td>
										<a>
											<xsl:attribute name="href">
												#<xsl:value-of select="@name" />
											</xsl:attribute>
											<xsl:value-of select="@name" />
										</a>
									</td>
									<td>
										<xsl:value-of select="count(testcase)" />
									</td>
									<td>
										<xsl:value-of select="count(testcase[@changes = 'Add'])" />
									</td>
									<td>
										<xsl:value-of select="count(testcase[@changes = 'Update'])" />
									</td>
									<td>
										<xsl:value-of select="count(testcase[@changes = 'Remove'])" />
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
							<table>
								<tr>
									<th>Case ID</th>
									<th>Priority</th>
									<th>Status</th>
									<th>Changes</th>
									<th>Source</th>
									<th>Description</th>
								</tr>
								<xsl:for-each select=".//suite">
									<xsl:sort select="@name" />
									<tr>
										<td colspan="6">
											<h3>Test Suite:
											<xsl:value-of select="@name" /></h3>
											<a>
												<xsl:attribute name="name">
													<xsl:value-of select="@name" />
												</xsl:attribute>
											</a>
										</td>
									</tr>
									<xsl:for-each select=".//testcase">
										<xsl:sort select="@changes" />
										<tr>
											<td>
												<xsl:value-of select="@id" />
											</td>
											<td>
												<xsl:value-of select="@priority" />
											</td>
											<td>
												<xsl:value-of select="@status" />
											</td>
											<td>
												<xsl:value-of select="@changes" />
											</td>
											<td>
												<xsl:value-of select="@source" />
											</td>
											<td>
												<xsl:value-of select=".//description" />
											</td>
										</tr>
									</xsl:for-each>
								</xsl:for-each>
							</table>
					</div>
				</div>
				<div id="goTopBtn">
					<a href="#top">
						<img border="0" src="./back_top.png" />
					</a>
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
