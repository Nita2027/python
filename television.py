class Television:
    """Represents TV with power channel volume and mute controls."""
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Initializes the TV with default settings.
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Turns TV on or off.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Mutes or unmutes the TV when it is on
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """Increases the channel when the TV is on.
        
        Return to min channel when max is reached.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """Decreases channel when TV is on.
        
        Return to max channel when min is reached.
        """
        if self.__status > Television.MIN_CHANNEL:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Increases volume and unmutes the TV when it is on.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decreases volume and unmutes the TV when it is on.
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Method to show the TV status.
        :return: TV status.
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'