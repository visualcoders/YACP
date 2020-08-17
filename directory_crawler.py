import os

#A class for crawling trough all sub and root directiories
class DirectoryCrawler(object):
    """
    Zero dependency(uses only built-in os package for it's file walker) directory crawler with optinal extension filter.
    Not optimized to be fair but this doesn't mean it'll always be like that
    """
    __slots__ = ['__trgt_dir', '__ext']
    #Constructor stores all parameters
    def __init__(self, trgt_dir: str, ext: str = None) -> None:
        """Initializer/Constructor for directory crawler"""
        self.__trgt_dir = trgt_dir
        self.__ext = ext

    #region CONTEXT_MANAGER_SUPPORT
    def __enter__(self):
        """Support for context managers, creates an instace"""
        return self

    def __exit__(self, exc_type, exc_val, tb):
        """Support for context managers, deletes the instance if Generator finishes"""
        if exc_type is GeneratorExit:
            self = None
            del(self)
            return False
        return True
    #endregion   
    #region CUSTOM_METHODS

    #Some accessors for making lifes easier
    def get_trgt_dir(self) -> str:  
        """An accessor method for getting target directory"""
        return self.__trgt_dir 
    def get_ext_filt(self) -> str: 
        """An accessor method for getting extension filter"""
        return self.__ext

    #Crawling extensions
    def crawl(self) -> str:
        """A generator method that yield filtered/non-filtered file with absolute path as string"""
        
        #Use os package's directory walker to get file directory data
        for root, dirs, files in os.walk(self.get_trgt_dir()):
            
            #Get all files in files
            for f in files:
                
                #Check if extenion filter is matching or just not fed extension filter
                if f.endswith(str(self.get_ext_filt())) or self.get_ext_filt() == "" or self.get_ext_filt() == None:
                    
                    #Get file's root directory
                    f = os.path.join(root, f)
                    
                    #Change backslash to python friendly normal slash
                    f = str(f).replace("\\", "/")

                    #Yield (return as iterable) file directory
                    yield f

    #endregion 
