from loguru import logger

# Disable logging by default for library usage.
# Application entry points (e.g., biofoundry_cli.cli) should call logger.enable("biofoundry_cli")
# to enable logging.
logger.disable("biofoundry_cli")
