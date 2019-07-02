import pandas as pd

print('Hello')
'''
cnxn = pyodbc.connect('DSN=LLB01DSS;UID=fbarboza;PWD=Cambio18')

# Copy to Clipboard for paste in Excel sheet
def copia (argumento):
    df=pd.DataFrame(argumento)
    df.to_clipboard(index=False,header=True)


tableResult = pd.read_sql("""SELECT 	A.PROD_ID, 
	    A.MERC_DSCRPTR_SDESC, 
	    A.MERC_DSCRPTR_ID, 
	    DSS.SRC_REF.SRC_LF_YR, 
	    DSS.SRC_REF.SRC_ID, 
	    LLB.PROD_DSPL_XREF.PROD_EXPSR_PG_NBR, 
	    DSS.SRC_REF.SRC_DESC, 
        DSS.SRC_REF.SRC_CGY_DESC 
        FROM 	DSS.PROD_REF A, 
	    LLB.PROD_DSPL_XREF, 
        DSS.SRC_REF 
        WHERE LLB.PROD_DSPL_XREF.PROD_EXPSR_IND = '1' and A.ITEM_ID = '188455' 	and 
	    LLB.PROD_DSPL_XREF.SRC_ID = DSS.SRC_REF.SRC_ID 
	    and 
	    LLB.PROD_DSPL_XREF.SRC_LF_YR = DSS.SRC_REF.SRC_LF_YR 
        and 
        LLB.PROD_DSPL_XREF.PROD_ID = A.PROD_ID""", cnxn)

#create a Excel file with the results
#df=pd.DataFrame(tableResult)
#df.to_excel("FileExample.xlsx",sheet_name='Results', index=False)'''
