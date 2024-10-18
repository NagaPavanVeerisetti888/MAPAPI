import pytest


from datetime import datetime
import os
# Generate timestamp
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
file_path = os.path.join("..", "reports", f"report_{timestamp}.html")
print(file_path)
report_path = file_path
# Ensure the reports directory exists
os.makedirs(os.path.dirname(report_path), exist_ok=True)
# Run pytest with the dynamically generated report filename
pytest.main(['--html=' + report_path])