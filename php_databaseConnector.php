class myPDO extends PDO {
	public function __construct() {
	  $settings = parse_ini_file('folder/db_info.ini',TRUE);
	  if (!$settings) throw new exception('Can not open ini file.');
	  $drv = $settings['database']['driver'];
	  $hst = $settings['database']['host'];
	  $sch = $settings['database']['schema'];
	  $usr = $settings['database']['username'];
	  $pwd = $settings['database']['password'];
	  $dns = $drv . ':host=' . $hst . ';dbname=' . $sch;
	  $options = array(
		PDO::MYSQL_ATTR_INIT_COMMAND => 'SET NAMES utf8',
	  );
	  parent::__construct($dns,$usr,$pwd,$options);
	}
}
