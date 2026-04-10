import re

from second_brain.app import LEVEL_ABBR, main


def test_main_logs_greeting(capfd):
    main()
    captured = capfd.readouterr()
    assert "Hello from second_brain!" in captured.err


class TestLevelAbbreviations:
    """LEVEL_ABBR maps every standard loguru level to a 3-letter code."""

    def test_all_standard_levels_present(self):
        expected = {"TRACE", "DEBUG", "INFO", "SUCCESS", "WARNING", "ERROR", "CRITICAL"}
        assert set(LEVEL_ABBR.keys()) == expected

    def test_all_abbreviations_are_three_characters(self):
        for level, abbr in LEVEL_ABBR.items():
            assert len(abbr) == 3, f"{level} abbreviation '{abbr}' is not 3 chars"

    def test_specific_mappings(self):
        assert LEVEL_ABBR["TRACE"] == "TRC"
        assert LEVEL_ABBR["DEBUG"] == "DBG"
        assert LEVEL_ABBR["INFO"] == "INF"
        assert LEVEL_ABBR["SUCCESS"] == "SUC"
        assert LEVEL_ABBR["WARNING"] == "WRN"
        assert LEVEL_ABBR["ERROR"] == "ERR"
        assert LEVEL_ABBR["CRITICAL"] == "CRT"


class TestStderrFormat:
    """stderr log lines must match the compact format."""

    def test_no_milliseconds_in_timestamp(self, capfd):
        main()
        captured = capfd.readouterr()
        # Milliseconds would appear as .NNN after seconds
        assert re.search(r"\.\d{3}", captured.err) is None

    def test_uses_abbreviated_level(self, capfd):
        main()
        captured = capfd.readouterr()
        assert "| INF |" in captured.err

    def test_pipe_separators_throughout(self, capfd):
        main()
        captured = capfd.readouterr()
        # The old format used " - " before the message; that must be gone
        assert " - " not in captured.err
        # Expect four pipe-separated fields
        line = captured.err.strip().splitlines()[-1]
        assert line.count("|") == 3

    def test_full_format_matches_target(self, capfd):
        main()
        captured = capfd.readouterr()
        line = captured.err.strip().splitlines()[-1]
        pattern = (
            r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"  # timestamp without ms
            r" \| [A-Z]{3}"                              # abbreviated level
            r" \| \S+:\S+:\d+"                           # module:function:line
            r" \| .+$"                                   # message
        )
        assert re.match(pattern, line), f"Line does not match target format: {line}"


class TestFileHandlerUnchanged:
    """The file handler must keep the default verbose loguru format."""

    def test_file_log_has_milliseconds(self, capfd, tmp_path):
        import os

        log_file = tmp_path / "test.log"
        os.environ["LOG_FILE"] = str(log_file)
        try:
            main()
        finally:
            os.environ.pop("LOG_FILE", None)

        content = log_file.read_text()
        # Default loguru format includes milliseconds as .NNN
        assert re.search(r"\.\d{3}", content), "File log should contain milliseconds"

    def test_file_log_has_full_level_name(self, capfd, tmp_path):
        import os

        log_file = tmp_path / "test.log"
        os.environ["LOG_FILE"] = str(log_file)
        try:
            main()
        finally:
            os.environ.pop("LOG_FILE", None)

        content = log_file.read_text()
        assert "INFO" in content
        # Full level name is padded to 8 chars in default format
        assert "INF" not in content.replace("INFO", "")
