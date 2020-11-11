package util

import java.io.File

object CommonUtil {

  def getFile(fileName: String): File = {
    new File(fileName)
  }

}
