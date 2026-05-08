FROM ruby:3.1

WORKDIR /site

COPY Gemfile Gemfile.lock ./
RUN gem install bundler && bundle install

COPY . .

EXPOSE 4000

CMD ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0"]
