FROM ruby:2.6

RUN mkdir /site
WORKDIR /site

RUN gem install bundler -v "~>2.0"

COPY ./Gemfile /site/Gemfile
COPY ./grape-theme.gemspec /site/grape-theme.gemspec

RUN bundle install

EXPOSE 4000


