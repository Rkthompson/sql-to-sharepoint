# sql-to-sharepoint
Pull data from SQL server and use it to add/delete records to/from a SharePoint list.

## Database Layer
---
### SQL Server - Database - Table

Using Python: SQLAlchemy library

### Actions:
1. Open Connection
2. Request Data
3. Close Connection

## Buisness Logic
---
### Object Models:

>Batch (One)

>ListItem (Many)

One Batch is created per call to Database as one Batch object
made of many ListItem objects.

The same Batch Model is used for two operations:
* Records to Delete.
* Records to Add.

Records to Delete: 
Selection of records in the database that have a status of closed from the
past 48 hours.  Becomes the *DeleteBatch*.

Records to Add:
Selection of records in the database that have a status of open.  Becomes the 
*AddBatch*.

## Presentation Layer
---
### Office365 | SharePoint List

Using Python MSAL, Request, and JSON libraries

### Request Authorization

Get token from Microsoft Identity Platform without user.

Use GRAPH API to connect to SharePoint list:
* Delete list items that are in *DeleteBatch*.
* Add list items from *AddBatch*.

**Ignore list items that have been added by a user**

