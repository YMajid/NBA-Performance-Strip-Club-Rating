package session

import com.typesafe.config.Config
import org.apache.spark.SparkConf
import org.apache.spark.sql.SparkSession

object SparkUtil {

  def createSparkSession(sparkConfig: Config): SparkSession = {

    val mode = sparkConfig.getString("mode")
    val appName = sparkConfig.getString("applicationName")
    val shufflePartitions = sparkConfig.getString("shufflePartitions")
    val sparkConf = new SparkConf()
      .setAppName(appName)
      .set("spark.sql.shuffle.partitions", shufflePartitions)

    SparkSession
      .builder()
      .master(mode)
      .config(sparkConf)
      .getOrCreate()

  }

}
