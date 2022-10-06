/*---file pre---*/
<%@ page isErrorPage="true" contentType="application/vnd.ms-excel;
        charset=euc-kr" %>
        
<%@ page language="java" import="java.sql.*, java.io.*, jxl.*" %>
<%
    String path = "C:\\";
    String filename = "Book1.xls";
    Workbook workbook = Workbook.getWorkbook(new File(path+"\\"+filename));
    Sheet sheet = workbook.getSheet(0);
    int col = sheet.getColumns();
    System.out.println("col"+col);
    int row = sheet.getRows();
    System.out.println("row"+row);
%>