"""Passthrough shim for fal extension."""
import sys

import structlog
from meltano.edk.logging import pass_through_logging_config
from fal_ext.extension import fal


def pass_through_cli() -> None:
    """Pass through CLI entry point."""
    pass_through_logging_config()
    ext = fal()
    ext.pass_through_invoker(
        structlog.getLogger("fal_invoker"),
        *sys.argv[1:] if len(sys.argv) > 1 else []
    )
