# Starting-with-Data-Engineering
Getting started with the Data Engineering, learning about data engineering tools and technology, Covering topics like Data Warehouse, Data Lakes, Analytics Engineering etc, Using techs like Kafka, DBT, Apache Spark, etc . Then at last will create a live project



PS C:\Users\gopal\OneDrive\Documents\GitHub\Starting-with-Data-Engineering> function prompt { "$(Split-Path -Leaf (Get-Location)) > " }
Starting-with-Data-Engineering > code $PROFILE
Starting-with-Data-Engineering > . $PROFILE
. : File C:\Users\gopal\OneDrive\Documents\WindowsPowerShell\Microsoft.PowerShe
ll_profile.ps1 cannot be loaded because running scripts is disabled on this 
system. For more information, see about_Execution_Policies at 
https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:3
+ . $PROFILE
+   ~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess

Starting-with-Data-Engineering > Get-ExecutionPolicy -Scope CurrentUser
Undefined

Starting-with-Data-Engineering > Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

Starting-with-Data-Engineering > Get-ExecutionPolicy -Scope CurrentUser
RemoteSigned

Starting-with-Data-Engineering > . $PROFILE
Starting-with-Data-Engineering > 