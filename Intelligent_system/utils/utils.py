import sys
from datetime import timedelta
from typing import Iterator, TextIO

from Intelligent_system.exception import CustomException

def write_srt(transcript: Iterator[dict], file: TextIO):
    """
    It takes a transcript and a file object, and writes the transcript to the file in SRT format -> SubRip subTitle

    Args:
      transcript (Iterator[dict]): Iterator[dict]
      file (TextIO): The file to write the transcript to.
    """
    try:
        for i, segment in enumerate(transcript, start=1):
            print(
                f"{i}\n"
                f"{format_timestamp(segment['start'], always_include_hours=True)} --> "
                f"{format_timestamp(segment['end'], always_include_hours=True)}\n"
                f"{segment['text'].strip().replace('-->', '->')}\n",
                file=file,
                flush=True,
            )
    except Exception as e:
        raise CustomException(e, sys)
    