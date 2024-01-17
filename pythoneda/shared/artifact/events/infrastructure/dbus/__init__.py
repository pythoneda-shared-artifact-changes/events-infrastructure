# vim: set fileencoding=utf-8
"""
pythoneda/shared/artifact/events/infrastructure/dbus/__init__.py

This file ensures pythoneda.shared.artifact.events.infrastructure.dbus is a package.

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
__path__ = __import__("pkgutil").extend_path(__path__, __name__)

DBUS_PATH = "/pythoneda/shared/artifact"

from .dbus_change_staged import DbusChangeStaged
from .dbus_committed_changes_pushed import DbusCommittedChangesPushed
from .dbus_committed_changes_tagged import DbusCommittedChangesTagged
from .dbus_staged_changes_committed import DbusStagedChangesCommitted
from .dbus_tag_pushed import DbusTagPushed
# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
