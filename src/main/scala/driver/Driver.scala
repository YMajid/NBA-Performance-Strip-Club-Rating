package driver

import com.typesafe.config.ConfigFactory
import com.typesafe.scalalogging.LazyLogging
import session.SparkUtil
import util.CommonUtil

object Driver extends App with LazyLogging {

  val sparkConfig = ConfigFactory.parseFile(CommonUtil.getFile("/home/yousif/Programming/NBA Strip Club/config/spark.conf"))
  val spark = SparkUtil.createSparkSession(sparkConfig)

  val df = spark.read.parquet("/home/yousif/Programming/NBA Strip Club/python/nba_api/allTeams.parquet")
  df.count()

}
