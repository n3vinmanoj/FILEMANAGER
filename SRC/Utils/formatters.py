from datetime import datetime

def format_size(bytes_size):
    """Format file size in human readable format"""
    if bytes_size == 0:
        return "0 Bytes"
    
    sizes = ["Bytes", "KB", "MB", "GB", "TB"]
    i = 0
    while bytes_size >= 1024 and i < len(sizes) - 1:
        bytes_size /= 1024
        i += 1
    
    return f"{bytes_size:.2f} {sizes[i]}"

def format_datetime(timestamp):
    """Format timestamp to readable date string"""
    try:
        if isinstance(timestamp, str):
            dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
        else:
            dt = datetime.fromtimestamp(timestamp / 1000 if timestamp > 1e10 else timestamp)
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except:
        return "Unknown"