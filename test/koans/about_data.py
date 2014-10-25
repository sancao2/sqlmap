#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *
from lib.core.data import paths
from lib.core.common import setPaths
from sqlmap import modulePath

from lib.core.data import cmdLineOptions
from lib.parse.cmdline import cmdLineParser
from lib.core.option import initOptions

from lib.core.data import kb
from lib.core.data import conf

from lib.core.data import logger


class AboutData(Koan):

    def test_paths_setPaths(self):
        self.assertEqual({}, paths)
        paths.SQLMAP_ROOT_PATH = modulePath()
#        self.assertEqual({'SQLMAP_ROOT_PATH': u'/home/k/Develop/sqlmap'}, paths)
        setPaths()
        self.maxDiff = None
        # self.assertDictContainsSubset({'COMMON_COLUMNS': u'/home/k/Develop/sqlmap/txt/common-columns.txt',
        #                                 'COMMON_OUTPUTS': u'/home/k/Develop/sqlmap/txt/common-outputs.txt',
        #                                 'COMMON_TABLES': u'/home/k/Develop/sqlmap/txt/common-tables.txt',
        #                                 'ERRORS_XML': u'/home/k/Develop/sqlmap/xml/errors.xml',
        #                                 'GENERIC_XML': u'/home/k/Develop/sqlmap/xml/banner/generic.xml',
        #                                 'INJECTIONS_XML': u'/home/k/Develop/sqlmap/xml/injections.xml',
        #                                 'LIVE_TESTS_XML': u'/home/k/Develop/sqlmap/xml/livetests.xml',
        #                                 'MSSQL_XML': u'/home/k/Develop/sqlmap/xml/banner/mssql.xml',
        #                                 'MYSQL_XML': u'/home/k/Develop/sqlmap/xml/banner/mysql.xml',
        #                                 'ORACLE_XML': u'/home/k/Develop/sqlmap/xml/banner/oracle.xml',
        #                                 'OS_SHELL_HISTORY': '/home/k/.sqlmap/os.hst',
        #                                 'PAYLOADS_XML': u'/home/k/Develop/sqlmap/xml/payloads.xml',
        #                                 'PGSQL_XML': u'/home/k/Develop/sqlmap/xml/banner/postgresql.xml',
        #                                 'QUERIES_XML': u'/home/k/Develop/sqlmap/xml/queries.xml',
        #                                 'SMALL_DICT': u'/home/k/Develop/sqlmap/txt/smalldict.txt',
        #                                 #'SQLMAP_CONFIG': u'/home/k/Develop/sqlmap/sqlmap-dieD.conf',
        #                                 'SQLMAP_DUMP_PATH': u'/home/k/.sqlmap/output/%s/dump',
        #                                 'SQLMAP_EXTRAS_PATH': u'/home/k/Develop/sqlmap/extra',
        #                                 'SQLMAP_FILES_PATH': u'/home/k/.sqlmap/output/%s/files',
        #                                 'SQLMAP_OUTPUT_PATH': u'/home/k/.sqlmap/output',
        #                                 'SQLMAP_PROCS_PATH': u'/home/k/Develop/sqlmap/procs',
        #                                 'SQLMAP_ROOT_PATH': u'/home/k/Develop/sqlmap',
        #                                 'SQLMAP_SHELL_HISTORY': '/home/k/.sqlmap/sqlmap.hst',
        #                                 'SQLMAP_SHELL_PATH': u'/home/k/Develop/sqlmap/shell',
        #                                 'SQLMAP_TAMPER_PATH': u'/home/k/Develop/sqlmap/tamper',
        #                                 'SQLMAP_TXT_PATH': u'/home/k/Develop/sqlmap/txt',
        #                                 'SQLMAP_UDF_PATH': u'/home/k/Develop/sqlmap/udf',
        #                                 'SQLMAP_WAF_PATH': u'/home/k/Develop/sqlmap/waf',
        #                                 'SQLMAP_XML_BANNER_PATH': u'/home/k/Develop/sqlmap/xml/banner',
        #                                 'SQLMAP_XML_PATH': u'/home/k/Develop/sqlmap/xml',
        #                                 'SQL_KEYWORDS': u'/home/k/Develop/sqlmap/txt/keywords.txt',
        #                                 'SQL_SHELL_HISTORY': '/home/k/.sqlmap/sql.hst',
        #                                 'USER_AGENTS': u'/home/k/Develop/sqlmap/txt/user-agents.txt',
        #                                 'WORDLIST': u'/home/k/Develop/sqlmap/txt/wordlist.zip'}, paths)
        #self.assertEqual(u'/home/k/Develop/sqlmap/sqlmap-YplE.conf', paths.SQLMAP_CONFIG)
        import os
        profileOutputFile = os.path.join(paths.SQLMAP_OUTPUT_PATH, "sqlmap_profile.raw")
        # self.assertEqual(u'/home/k/.sqlmap/output/sqlmap_profile.raw', profileOutputFile)
        paths.SQLMAP_FILES_PATH = os.path.join(paths.SQLMAP_OUTPUT_PATH, "%s", "files")
        # self.assertEqual(u'/home/k/.sqlmap/output/%s/files', paths.SQLMAP_FILES_PATH)

    # def test_cmdLineOptions_initOptions_h(self):
    #     import sys
    #     try:
    #         sys.argv = ["-h"]
    #         cmdLineOptions.update(cmdLineParser().__dict__)
    #         initOptions(cmdLineOptions)
    #     except SystemExit as e:
    #         self.assertEqual(0, e[0])

    def test_cmdLineOptions_initOptions_xx(self):
        import sys
        self.assertEqual({}, cmdLineOptions)
        try:
            sys.argv = ["-u", "https://passport.baidu.com/v2/?reg&tpl=tb&u=http://tieba.baidu.com"]
            cmdLineOptions.update(cmdLineParser().__dict__)
            initOptions(cmdLineOptions)
        except Exception as e:
            self.assertEqual("unable to access item 'SQL_KEYWORDS'", e[0])
            logger.exception("just test logger.exception! ")
        self.maxDiff = None
        self.assertDictEqual({'advancedHelp': None,
                              'agent': None,
                              'alert': None,
                              'answers': None,
                              'authCred': None,
                              'authPrivate': None,
                              'authType': None,
                              'batch': None,
                              'beep': None,
                              'binaryFields': None,
                              'bulkFile': None,
                              'charset': None,
                              'checkTor': None,
                              'checkWaf': None,
                              'cleanup': None,
                              'code': None,
                              'col': None,
                              'commonColumns': None,
                              'commonTables': None,
                              'configFile': None,
                              'cookie': None,
                              'cookieDel': None,
                              'cpuThrottle': None,
                              'crawlDepth': None,
                              'csvDel': None,
                              'dFile': None,
                              'data': None,
                              'db': None,
                              'dbms': None,
                              'dbmsCred': None,
                              'delay': None,
                              'dependencies': None,
                              'direct': None,
                              'disableColoring': None,
                              'dnsName': None,
                              'dropSetCookie': None,
                              'dummy': None,
                              'dumpAll': None,
                              'dumpFormat': None,
                              'dumpTable': None,
                              'dumpWhere': None,
                              'eta': None,
                              'evalCode': None,
                              'excludeCol': None,
                              'excludeSysDbs': None,
                              'extensiveFp': None,
                              'firstChar': None,
                              'flushSession': None,
                              'forceDns': None,
                              'forceSSL': None,
                              'forms': None,
                              'freshQueries': None,
                              'getAll': None,
                              'getBanner': None,
                              'getColumns': None,
                              'getComments': None,
                              'getCount': None,
                              'getCurrentDb': None,
                              'getCurrentUser': None,
                              'getDbs': None,
                              'getHostname': None,
                              'getPasswordHashes': None,
                              'getPrivileges': None,
                              'getRoles': None,
                              'getSchema': None,
                              'getTables': None,
                              'getUsers': None,
                              'googleDork': None,
                              'googlePage': None,
                              'headers': None,
                              'hexConvert': None,
                              'host': None,
                              'hpp': None,
                              'identifyWaf': None,
                              'ignore401': None,
                              'ignoreProxy': None,
                              'invalidBignum': None,
                              'invalidLogical': None,
                              'invalidString': None,
                              'isDba': None,
                              'keepAlive': None,
                              'lastChar': None,
                              'level': None,
                              'limitStart': None,
                              'limitStop': None,
                              'liveTest': None,
                              'loadCookies': None,
                              'logFile': None,
                              'mnemonics': None,
                              'mobile': None,
                              'msfPath': None,
                              'noCast': None,
                              'noEscape': None,
                              'notString': None,
                              'nullConnection': None,
                              'optimize': None,
                              'os': None,
                              'osBof': None,
                              'osCmd': None,
                              'osPwn': None,
                              'osShell': None,
                              'osSmb': None,
                              'outputDir': None,
                              'pageRank': None,
                              'paramDel': None,
                              'parseErrors': None,
                              'pickledOptions': None,
                              'pivotColumn': None,
                              'predictOutput': None,
                              'prefix': None,
                              'privEsc': None,
                              'profile': None,
                              'proxy': None,
                              'proxyCred': None,
                              'proxyFile': None,
                              'purgeOutput': None,
                              'query': None,
                              'rFile': None,
                              'rParam': None,
                              'randomAgent': None,
                              'referer': None,
                              'regAdd': None,
                              'regData': None,
                              'regDel': None,
                              'regKey': None,
                              'regRead': None,
                              'regType': None,
                              'regVal': None,
                              'regexp': None,
                              'requestFile': None,
                              'retries': None,
                              'risk': None,
                              'runCase': None,
                              'saFreq': None,
                              'safUrl': None,
                              'saveCmdline': None,
                              'scope': None,
                              'search': None,
                              'secondOrder': None,
                              'sessionFile': None,
                              'shLib': None,
                              'showVersion': None,
                              'sitemapUrl': None,
                              'skip': None,
                              'skipUrlEncode': None,
                              'smart': None,
                              'smokeTest': None,
                              'sqlFile': None,
                              'sqlShell': None,
                              'sqlmapShell': None,
                              'stopFail': None,
                              'string': None,
                              'suffix': None,
                              'tamper': None,
                              'tbl': None,
                              'tech': None,
                              'testFilter': None,
                              'testParameter': None,
                              'textOnly': None,
                              'threads': None,
                              'timeSec': None,
                              'timeout': None,
                              'titles': None,
                              'tmpPath': None,
                              'tor': None,
                              'torPort': None,
                              'torType': None,
                              'trafficFile': None,
                              'uChar': None,
                              'uCols': None,
                              'uFrom': None,
                              'udfInject': None,
                              'updateAll': None,
                              'url': u'https://passport.baidu.com/v2/?reg&tpl=tb&u=http://tieba.baidu.com',
                              'user': None,
                              'verbose': None,
                              'wFile': None,
                              'wizard': None}, cmdLineOptions)
        self.assertDictEqual({'authPassword': None,
                              'authUsername': None,
                              'boundaries': [],
                              'cj': None,
                              'dbmsConnector': None,
                              'dbmsHandler': None,
                              'dnsServer': None,
                              'dumpPath': None,
                              'hashDB': None,
                              'hashDBFile': None,
                              'hostname': None,
                              'httpHeaders': [],
                              'ipv6': False,
                              'multipleTargets': False,
                              'outputPath': None,
                              'paramDict': {},
                              'parameters': {},
                              'path': None,
                              'port': None,
                              'proxyList': [],
                              'resultsFP': None,
                              'resultsFilename': None,
                              'scheme': None,
                              'tests': [],
                              'trafficFP': None,
                              'wFileType': None}, conf)
    # https://docs.python.org/2/howto/logging.html?highlight=logger#logging-howto
    def test_logger(self):
        self.assertEqual(['__class__', '__delattr__', '__dict__', '__doc__',
                          '__format__', '__getattribute__', '__hash__', '__init__',
                          '__module__', '__new__', '__reduce__', '__reduce_ex__',
                          '__repr__', '__setattr__', '__sizeof__', '__str__',
                          '__subclasshook__', '__weakref__', '_log', 'addFilter',
                          'addHandler', 'callHandlers', 'critical', 'debug',
                          'disabled', 'error', 'exception', 'fatal', 'filter',
                          'filters', 'findCaller', 'getChild', 'getEffectiveLevel',
                          'handle', 'handlers', 'info', 'isEnabledFor', 'level', 'log',
                          'makeRecord', 'manager', 'name', 'parent', 'propagate',
                          'removeFilter', 'removeHandler', 'root', 'setLevel', 'warn',
                          'warning'], dir(logger))
        logger.debug("DEBUG message goes")
        logger.info("INFO message goes")
        self.assertEqual(False, logger == logger.root)
        self.assertEqual("sqlmapLog", logger.name)
        self.assertEqual(30, logger.level)
        self.assertEqual(30, logger.getEffectiveLevel())
        self.assertEqual(False, logger.isEnabledFor(29))
        self.assertEqual(True, logger.isEnabledFor(31))
        self.assertEqual(1, logger.propagate)
        # logging.Manager
        self.assertEqual(['__class__', '__delattr__', '__dict__', '__doc__',
                          '__format__', '__getattribute__', '__hash__', '__init__',
                          '__module__', '__new__', '__reduce__', '__reduce_ex__',
                          '__repr__', '__setattr__', '__sizeof__', '__str__',
                          '__subclasshook__', '__weakref__', '_fixupChildren',
                          '_fixupParents', 'disable', 'emittedNoHandlerWarning',
                          'getLogger', 'loggerClass', 'loggerDict', 'root', 'setLoggerClass'],
                         dir(logger.manager))
        self.assertEqual(True, logger.manager.loggerDict['sqlmapLog'] == logger)
        self.assertEqual(30, logger.manager.loggerDict['ClientForm'].getEffectiveLevel())
        self.assertEqual(0, logger.manager.loggerDict['ClientForm'].level)
        self.assertEqual(False, logger.manager.loggerDict['ClientForm'] == logger.root)
        # logging.filters
        self.assertEqual([], logger.filters)
        # ColorizingStreamHandler
        from thirdparty.ansistrm.ansistrm import ColorizingStreamHandler
        self.assertEqual(['__class__', '__delattr__', '__dict__', '__doc__',
                          '__format__', '__getattribute__', '__hash__', '__init__',
                          '__module__', '__new__', '__reduce__', '__reduce_ex__',
                          '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
                          '__weakref__', '_name', 'acquire', 'addFilter', 'close',
                          'color_map','colorize', 'createLock', 'csi', 'disable_coloring',
                          'emit', 'filter','filters', 'flush', 'format', 'formatter',
                          'get_name', 'handle', 'handleError', 'is_tty', 'level',
                          'level_map', 'lock', 'name', 'output_colorized', 'release',
                          'removeFilter', 'reset', 'setFormatter', 'setLevel',
                          'set_name', 'stream'], dir(logger.handlers[0]))
        self.assertEqual(True, logger.handlers[0].is_tty)
        # CRITICAL = 50
        # FATAL = CRITICAL
        # ERROR = 40
        # WARNING = 30 --default
        # WARN = WARNING
        # INFO = 20
        # DEBUG = 10
        # NOTSET = 0
        # LOGGER_HANDLER.level_map[logging.getLevelName("PAYLOAD")] = (None, "cyan", False)
        # LOGGER_HANDLER.level_map[logging.getLevelName("TRAFFIC OUT")] = (None, "magenta", False)
        # LOGGER_HANDLER.level_map[logging.getLevelName("TRAFFIC IN")] = ("magenta", None, False)
        self.assertEqual({7: ('magenta', None, False),
                          40: (None, 'red', False),
                          9: (None, 'cyan', False),
                          10: (None, 'blue', False),
                          8: (None, 'magenta', False),
                          50: ('red', 'white', False),
                          20: (None, 'green', False),
                          30: (None, 'yellow', False)},
                         logger.handlers[0].level_map)
