# Python Import Alphabetizer

I like having my python imports in alphabetical order. This tool does that.

### Before:
```py
import base64
from cmath import sqrt
import asyncio
```

### After:
```py
import asyncio
import base64
from cmath import sqrt
```

## How to use:
1. Add any files or folders you don't want changed to `toskip.txt`
1. Start `run.py` and enter the root directory to start from.

_Note: this tool changes every '.py' file in the specified directory as well as subdirectories, but it only rearranges lines before the first non-import line_