# vim: set fileencoding=utf-8
"""
pythoneda/shared/artifact/events/infrastructure/dbus/dbus_docker_image_failed.py

This file defines the DbusDockerImageFailed class.

Copyright (C) 2024-today rydnr's pythoneda-shared-artifact/events-infrastructure

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
from dbus_next import Message
from dbus_next.service import ServiceInterface, signal
import json
from pythoneda.shared import BaseObject, Event
from pythoneda.shared.artifact.events import DockerImageFailed
from pythoneda.shared.artifact.events.infrastructure.dbus import DBUS_PATH
from typing import List


class DbusDockerImageFailed(BaseObject, ServiceInterface):
    """
    D-Bus interface for DockerImageFailed.

    Class name: DbusDockerImageFailed

    Responsibilities:
        - Define the d-bus interface for the DockerImageFailed event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusDockerImageFailed.
        """
        super().__init__("Pythoneda_Artifact_DockerImageFailed")

    @signal()
    def DockerImageFailed(
        self,
        imageName: "s",
        imageVersion: "s",
        cause: "s",
    ):
        """
        Defines the DockerImageFailed d-bus signal.
        :param imageName: The image name.
        :type imageName: str
        :param imageVersion: The version.
        :type imageVersion: str
        :param cause: The error cause.
        :type cause: str
        """
        pass

    @property
    def path(self) -> str:
        """
        Retrieves the d-bus path.
        :return: Such value.
        :rtype: str
        """
        return DBUS_PATH

    def build_path(self, event: Event) -> str:
        """
        Retrieves the d-bus path for given event.
        :param event: The event.
        :type event: pythoneda.shared.Event
        :return: Such value.
        :rtype: str
        """
        return DBUS_PATH + "/" + event.image_name.replace("-", "_")

    @classmethod
    def transform(cls, event: DockerImageFailed) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythoneda.shared.artifact.events.DockerImageFailed
        :return: The event information.
        :rtype: List[str]
        """
        return [
            event.image_name,
            event.image_version,
            json.dumps(event.metadata, ensure_ascii=False),
            event.cause,
            json.dumps(event.previous_event_ids),
            event.id,
        ]

    @classmethod
    def sign(cls, event: DockerImageFailed) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythoneda.shared.artifact.events.DockerImagFailed
        :return: The signature.
        :rtype: str
        """
        return "sssss"

    @classmethod
    def parse(cls, message: Message) -> DockerImageFailed:
        """
        Parses given d-bus message containing a DockerImageFailed event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The DockerImageFailed event.
        :rtype: pythoneda.shared.artifact.events.DockerImagFailed
        """
        image_name,
        image_version,
        metadata,
        cause,
        prev_event_ids,
        event_id = message.body
        return DockerImageFailed(
            image_name,
            image_version,
            json.loads(metadata),
            cause,
            json.loads(prev_event_ids),
            event_id,
        )


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
