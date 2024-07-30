# Launch a new browser instance with custom options
browser = p.chromium.launch(
    headless=False,  # Run the browser in headful mode
    viewport={'width': 1920, 'height': 1080},  # Set the viewport size
    ignoreHTTPSErrors=True,  # Ignore HTTPS errors
    proxy={'server': 'http://your-proxy-server:port'}  # Set network proxy settings
)
