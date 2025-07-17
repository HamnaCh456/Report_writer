from typing import Type    
from crewai.tools import BaseTool    
from pydantic import BaseModel, Field       
from firecrawl import FirecrawlApp 
    
class MyToolInput(BaseModel):    
    """Input schema for the web scraper tool"""    
    url: str = Field(..., description="The URL to scrape content from")    
    
class MyCustomTool(BaseTool):    
    name: str = "Website_Scraper"    
    description: str = "It scrapes the content of a website and returns the content in markdown format. Pass the URL as the 'url' parameter."    
    args_schema: Type[BaseModel] = MyToolInput    
       
    def _run(self, url: str) -> str:    
        if not url:
            raise ValueError("Missing 'url' in input.")
        app = FirecrawlApp(api_key="NA")# Scrape a website:
        scrape_result = app.scrape_url(url, formats=['markdown'])
        return scrape_result.markdown
      
