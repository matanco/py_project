class ApplicationController < ActionController::Base
  # Prevent CSRF attacks by raising an exception.
  # For APIs, you may want to use :null_session instead.
  protect_from_forgery with: :exception


  before_action :pull_data
  before_action :split_by_place

  def pull_data
    Aws.config.update({
                          region: "us-east-2"
                      })

    dynamodb = Aws::DynamoDB::Client.new

    table_name = "passblind1"

    params = {
        table_name: table_name,
    }

    @result = dynamodb.scan(params)
  end

  def split_by_place
    @places = []

    @result.items.each { |r| @places << r["place"] }

    @counts = Hash.new(0)
    @places.each { |name| @counts[name] += 1 }
  end

end
