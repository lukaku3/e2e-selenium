java -Xms1024m -Dwebdriver.chrome.driver=chromedriver.exe -jar -Dwebdriver.edge.driver=MicrosoftWebDriver.exe -Dwebdriver.ie.driver=x64\IEDriverServer.exe  -Dwebdriver.gecko.driver=x64\geckodriver.exe ..\selenium-server-standalone-3.141.59.jar -host 192.168.100.101 -role node  -hub http://192.168.100.101:4444/grid/register