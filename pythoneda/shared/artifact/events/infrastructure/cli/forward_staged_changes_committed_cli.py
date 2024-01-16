# vim: set fileencoding=utf-8
"""
pythoneda/shared/artifact/events/infrastructure/cli/forward_staged_changes_committed_cli.py

This file defines the ForwardStagedChangesCommittedCli class.

Copyright (C) 2023-today rydnr's pythoneda-shared-artifact/events-infrastructure

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import argparse
from pythoneda.shared import Event, EventEmitter, listen, Ports
from pythoneda.shared.artifact.events import Change, StagedChangesCommitted
from pythoneda.shared.git import GitCommit, GitDiff, GitRepo
from pythoneda.shared.infrastructure.cli import ForwardEventCli
import sys


class ForwardStagedChangesCommittedCli(ForwardEventCli):

    """
    A CLI handler that forwards StagedChangesCommitted events.

    Class name: ForwardStagedChangesCommittedCli

    Responsibilities:
        - Build events from information from the CLI, and forwards them.

    Collaborators:
        - pythoneda.shared.application.PythonEDA: To initialize this class.
    """

    def __init__(self):
        """
        Creates a new ForwardStagedChangesCommittedCli.
        """
        super().__init__("Forwards StagedChangesCommitted events")

    def add_arguments(self, parser: argparse.ArgumentParser):
        """
        Defines the specific CLI arguments.
        :param parser: The parser.
        :type parser: argparse.ArgumentParser
        """
        parser.add_argument(
            "-r", "--repository-folder", required=True, help="The repository folder"
        )

    def build_event(self, app, args: argparse.Namespace) -> Event:
        """
        Builds a StagedChangesCommitted event from the information specified from the command line.
        :param app: The PythonEDA instance.
        :type app: pythoneda.shared.application.PythonEDA
        :param args: The CLI args.
        :type args: argparse.Namespace
        :return: The event.
        :rtype: pythoneda.shared.Event
        """
        if not args.repository_folder:
            print(f"-r|--repository-folder is mandatory")
            sys.exit(1)
        else:
            git_repo = GitRepo.from_folder(args.repository_folder)
            change = Change.from_unidiff_text(
                GitDiff(args.repository_folder).committed_diff(),
                git_repo.url,
                git_repo.rev,
                args.repository_folder,
            )
            hash_value, diff, message = GitCommit(
                args.repository_folder
            ).latest_commit()
            result = StagedChangesCommitted(message, change, hash_value)
        return result
