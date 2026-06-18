import pytest
import shutil
import sys

from utils.api_client import APIClient
from utils.logger import logger

total_tests = 0
passed_tests = 0
failed_tests = 0
total_collected = 0

# ANSI colors
_GREEN = "\033[32m"
_RED = "\033[31m"
_RESET = "\033[0m"


@pytest.fixture
def api_client():

    client = APIClient()

    yield client

    client.close()


def pytest_sessionstart(session):

    logger.info("=" * 80)
    logger.info("STARTING TEST EXECUTION")
    logger.info("=" * 80)


def pytest_runtest_logreport(report):

    global total_tests
    global passed_tests
    global failed_tests
    global total_collected

    if report.when == "call":

        # Count completed tests (report indicates test outcome)
        total_tests += 1

        if report.passed:
            passed_tests += 1
            logger.info(f"PASSED -> {report.nodeid}")

        elif report.failed:
            failed_tests += 1
            logger.error(f"FAILED -> {report.nodeid}")

        # Update and print right-aligned progress line
        completed = passed_tests + failed_tests

        pct = 0.0
        # Ensure we have a denominator; try terminal reporter if needed
        if not total_collected:
            try:
                tr = report.config.pluginmanager.get_plugin("terminalreporter")
                possible = getattr(tr, "numcollected", None) or getattr(tr, "_numcollected", None)
                if possible:
                    total_collected = possible
            except Exception:
                pass

        if total_collected:
            pct = (completed / total_collected) * 100

        # Build colored status
        status = (
            f"PASSED: {_GREEN}{passed_tests}{_RESET} "
            f"FAILED: {_RED}{failed_tests}{_RESET} "
            f"| {completed}/{total_collected} {pct:.2f}%"
        )

        # Right-align to terminal width
        try:
            cols = shutil.get_terminal_size().columns
        except Exception:
            cols = 80

        if len(status) < cols:
            padding = " " * (cols - len(status))
        else:
            padding = ""

        # Print status as its own line aligned to the right
        sys.stdout.write(padding + status + "\n")
        sys.stdout.flush()


def pytest_sessionfinish(
        session,
        exitstatus
):

    logger.info("=" * 80)

    logger.info(
        f"TOTAL TESTS : {total_tests}"
    )

    logger.info(
        f"PASSED      : {passed_tests}"
    )

    logger.info(
        f"FAILED      : {failed_tests}"
    )

    if total_tests:

        pass_rate = (passed_tests / total_tests) * 100

        logger.info(f"PASS RATE   : {pass_rate:.2f}%")

    logger.info("=" * 80)


def pytest_collection_finish(session):
    """Capture total collected tests for progress percentage calculations."""

    global total_collected
    total_collected = session.testscollected


def pytest_collection_modifyitems(session, config, items):
    """Alternate hook to reliably capture collected items count."""

    global total_collected
    try:
        total_collected = len(items)
    except Exception:
        # fallback to session attribute
        total_collected = getattr(session, "testscollected", 0)


def pytest_collection_modifyitems(config, items):
    """Compatibility overload: some pytest versions call this signature."""

    global total_collected
    try:
        total_collected = len(items)
    except Exception:
        total_collected = 0