description = read.csv('comedy-all-descriptions.csv', header = F, encoding="UTF-8")
des = data.frame(description)
des = sapply(des, function(x) as.character(x))
library(tm)
des = des[,1]
des = data.frame(des)
getSources()
help(VectorSource)
des2 = VCorpus(VectorSource(des[,1])) #create the volatile corpus
num.docs = length(des2)
num.docs
#text transformations
# all to lower case
des2 = tm_map(des2, content_transformer(tolower))
#test
as.character(des2[[5]])
#remove punctuation
des2 = tm_map(des2, content_transformer(removePunctuation))
#remove numbers
des2 = tm_map(des2, content_transformer(removeNumbers))
#remove stopwords
des2 = tm_map(des2, removeWords, stopwords("english"))
#remove white space after other transformations
des2 = tm_map(des2, content_transformer(stripWhitespace))

#test = des2
#aaa = data.frame(test)
#write.csv(des2, file = "yourfile.csv", row.names = FALSE)

###save(des2,file = "cleaned-des.txt")

#create the document term matrix, which has a row for each document, 
#  and a column for each term/word
des2.dtm = DocumentTermMatrix(des2)
dim(des2.dtm)  # shows the number of docs and terms (in that order)
des2.dtm  # give basic summary info (more detailed than above) 
#find the more frequent terms
findFreqTerms(des2.dtm, lowfreq=600)  #show only those with freq 50 or higher
#get full details on terms, doesn't work for large matrix
#term.freq =colSums(as.matrix(des2.dtm), na.rm = T)
#another
library(slam)
term.freq = slam::col_sums(des2.dtm, na.rm = T)
top = term.freq[order(term.freq, decreasing=T)]  # in order of decreasing freq
# let us make a dataframe of it
term.df = data.frame(word=names(top), freq = top)


#subset terms with top 26 freqs
top_freq = subset(term.df, freq>400)
write.csv(top_freq, file = "comedy.csv", row.names = F)
str(top_freq)
#plot the frequency of the terms
library(ggplot2)
#show only those with freq 50 or higher
ggplot(top_freq, aes(word, freq)) + 
    geom_bar(stat="identity") +
    theme(axis.text.x=element_text(angle=45, hjust=1, size=20))
#make a word cloud
library(wordcloud)
set.seed(367)

#color
pal = c("#fc9272","#045a8d","#de2d26")
pal_2 = c("#7fcdbb","#41b6c4","#2c7fb8","#253494")
#wordcloud(top_freq$word, top_freq$freq, colors=pal)
wordcloud(top_freq$word, top_freq$freq, colors=brewer.pal(7, "Set1"))

care = read.csv('comedy-care-about.csv', header = T, encoding="UTF-8")
wordcloud(care$word, care$freq,colors=pal)

wordcloud() 

