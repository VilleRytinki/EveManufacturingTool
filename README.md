EveManufacturingTool

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
