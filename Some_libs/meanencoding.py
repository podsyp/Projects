from sklearn.base import BaseEstimator

class MeanEncoding(BaseEstimator):
    """
    Здесь мы делаем самый простой targetencoding
    """
    
    def __init__(self, feature, C=0.1):
        self.C = C
        self.feature = feature
        
    def fit(self, X_train, y_train):
        
        df = pd.DataFrame({'feature': X_train[self.feature], 'target': y_train}).dropna()
        
        self.global_mean = df.target.mean()
        mean = df.groupby('feature').target.mean()
        size = df.groupby('feature').target.size()
        
        self.encoding = (self.global_mean * self.C + mean * size) / (self.C + size)
    
    def transform(self, X_test):
        
        X_test[self.feature] = X_test[self.feature].map(self.encoding).fillna(self.global_mean).values
        
        return X_test
    
    def fit_transform(self, X_train, y_train):
        
        df = pd.DataFrame({'feature': X_train[self.feature], 'target': y_train}).dropna()
        
        self.global_mean = df.target.mean()
        mean = df.groupby('feature').target.mean()
        size = df.groupby('feature').target.size()
        self.encoding = (self.global_mean * self.C + mean * size) / (self.C + size)
        
        X_train[self.feature] = X_train[self.feature].map(self.encoding).fillna(self.global_mean).values
        
        return X_train
		
#me = MeanEncoding('gender', C=1)
#me.fit(tmp_df, tmp_df['target'])
#df_clients = me.transform(df_clients)
