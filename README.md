EveManufacturingTool

The purpose of this project is to develop an app which i could use daily, and to train my Data Engineering skills.
Tool for Eve Online to help with manufacturing process.
This tool will use the ESI OpenAPI for EVE online.
ESI documentation: https://esi.evetech.net/ui/

Based on how the ESI works, the idea of the workflow is:
- extract type id's
- use these id numbers to get item data for each item
- Transform the data to match the needs of this program as there is a lot of information
- get market prices for each item using market_group_id
- calculate the price of the build
- get the selling price of an item
- calculate the overhead
- determine if the build is profitable and by how much.

Current features:
  overhead calculation of a manufacturing process.
  gets data from ESI endpoints.
  
On consideration:
 - Maybe need a way to determine value per m3 aswell? There is a value factor in volume as bigger items are harder to transport, so the more expensive items might not make the most amount of money per m3.
