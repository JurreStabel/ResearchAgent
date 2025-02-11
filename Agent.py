import nest_asyncio
nest_asyncio.apply()

from llama_cloud_services import LlamaParse
from llama_index.core import SimpleDirectoryReader

parser = LlamaParse(
    api_key="llx-tmRcPt15jxP0giZhiHKGKfyAgb3dJLkKMsSGwixVRK7QnBPI",  # Alternatively, set as env var LLAMA_CLOUD_API_KEY
    result_type="markdown",  # Options: "markdown" or "text"
    verbose=True,
)

file_extractor = {".pdf": parser}

# Provide the directory containing your PDF(s)
documents = SimpleDirectoryReader(
    r"C:\Users\jurre\OneDrive\Documenten\ResearchAgent\papers", 
    file_extractor=file_extractor
).load_data()
