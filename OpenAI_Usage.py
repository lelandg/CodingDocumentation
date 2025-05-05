# Usage.py
# This script retrieves the usage data for a specific date range using the OpenAI API.

# First, make sure to set your OpenAI API key in your environment variables.
# [Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "<your-secret-key>", "User")
# Mac/Linux:
# export OPENAI_API_KEY="<your-secret-key>"
# If you’re building a Streamlit app, you can also put it in ~/.streamlit/secrets.toml or in your project’s .streamlit/secrets.toml under a key called OPENAI_API_KEY. Streamlit will pick that up automatically, but behind the scenes it still uses the same environment-variable mechanism (it injects it into os.environ).
# However, *do not* put your API key in your public repository!** This is a security risk and can lead to unauthorized usage of your OpenAI account.
# **The first thing I do when testing locally is to add ".streamlit/secrets.toml" to my .gitignore file.**

import os
import openai
from datetime import date

openai.api_key = os.getenv("OPENAI_API_KEY")

# Set the date range you want to query
start_date = date(2025, 5, 1).isoformat()   # e.g. 2025-05-01
end_date   = date(2025, 5, 4).isoformat()   # e.g. 2025-05-04

usage = openai.Usage.list(
    start_date=start_date,
    end_date=end_date,
)
print(usage)
